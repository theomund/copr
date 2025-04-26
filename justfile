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
all: lint build

# Build the project packages.
build: (rpm "erlang") (rpm "gleam") (rpm "limine") (rpm "vale")

# Clean the project tree.
clean:
    rm -rf target/

# Submit a build within COPR.
copr package: (srpm package)
    copr-cli build theomund/copr target/SRPMS/{{ package }}-*.src.rpm

# Deploy the project packages.
deploy: (copr "erlang") (copr "gleam") (copr "limine") (copr "vale")

# Run the project linters.
lint: rpmlint vale yamllint

# Build an RPM package.
rpm package: (srpm package)
    rpmbuild --rebuild --define "_topdir $(pwd)/target" target/SRPMS/{{ package }}-*.src.rpm

# Run the RPM linter.
rpmlint:
    rpmlint src/

# Retrieve the RPM source archive.
source package: setup
    spectool -Rg --define "_topdir $(pwd)/target" src/{{ package }}.spec

# Build a source RPM package.
srpm package: (source package)
    rpmbuild -bs --define "_topdir $(pwd)/target" src/{{ package }}.spec

# Setup the RPM build tree.
setup:
    mkdir -p target/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}

# Run the prose linter.
vale:
    vale sync
    vale README.md

# Run the YAML linter.
yamllint:
    yamllint .github/workflows/
