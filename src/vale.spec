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

Name:          vale
Version:       3.11.2
Release:       3%{?dist}
Summary:       Command-line tool that brings code-like linting to prose
URL:           https://%{name}.sh
Source:        https://github.com/errata-ai/%{name}/releases/download/v%{version}/%{name}_%{version}_Linux_64-bit.tar.gz
License:       MIT

%global debug_package %{nil}

%description
Vale is a command-line tool that brings code-like linting to prose. It's fast,
cross-platform, and highly customizable.

%prep
%setup -qc

%build

%check

%install
install -Dpvm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc README.md
%license LICENSE

%changelog
* Sat May 03 2025 Theomund <34360334+theomund@users.noreply.github.com> - 3.11.2-3
- Revert back to building using the pre-built binary.
* Fri Apr 25 2025 Theomund <34360334+theomund@users.noreply.github.com> - 3.11.2-2
- Build directly from the source code.
* Wed Apr 23 2025 Theomund <34360334+theomund@users.noreply.github.com> - 3.11.2-1
- Initial package.
