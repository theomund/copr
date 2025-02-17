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
build: srpm rpm

# Clean the project tree.
clean:
    git clean -fdx

# Submit a build within COPR.
copr:
    packit build in-copr

# Deploy the project packages.
deploy: copr

# Run the project linters.
lint: packit rpmlint vale yamllint

# Run the Packit linter.
packit:
    packit validate-config

# Build the RPM packages.
rpm:
    packit build locally

# Run the RPM linter.
rpmlint:
    rpmlint .

# Build the source RPM packages.
srpm:
    packit srpm

# Run the prose linter.
vale:
    vale sync
    vale README.md

# Run the YAML linter.
yamllint:
    yamllint .github/workflows .packit.yml
