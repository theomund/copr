# COPR - Packages for Fedora COPR.
# Copyright (C) 2025 Theomund
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# Run all CI/CD stages.
all: lint build verify

# Build the project packages.
build: (rpm "limine") (rpm "vale")

# Clean the project tree.
clean:
    rm -rf target/

# Submit a build within COPR.
copr package: (srpm package)
    copr-cli build theomund/copr target/{{ package }}/srpm/*.src.rpm

# Deploy the project packages.
deploy: (copr "limine") (copr "vale")

# Run the project linters.
lint: vale yamllint

# Build an RPM package.
rpm package: (srpm package)
    mock --rebuild --resultdir target/{{ package }}/rpm target/{{ package }}/srpm/*.src.rpm

# Run the RPM linter.
rpmlint package: (rpm package)
    rpmlint target/{{ package }}/rpm/*.rpm

# Retrieve the RPM source archive.
source package:
    spectool -gC target/{{ package }}/source src/{{ package }}.spec

# Build a source RPM package.
srpm package: (source package)
    mock --buildsrpm --resultdir target/{{ package }}/srpm --sources target/{{ package }}/source --spec src/{{ package }}.spec

# Run the prose linter.
vale:
    vale sync
    vale README.md

# Verify the RPM package quality.
verify: (rpmlint "limine") (rpmlint "vale")

# Run the YAML linter.
yamllint:
    yamllint .github/workflows/
