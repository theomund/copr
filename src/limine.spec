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

Name:          limine
Version:       9.2.3
Release:       1%{?dist}
Summary:       Modern, advanced, portable, multiprotocol bootloader and boot manager
URL:           https://%{name}-bootloader.org
Source:        https://github.com/%{name}-bootloader/%{name}/archive/refs/tags/v%{version}-binary.tar.gz
License:       BSD-2-Clause
BuildRequires: gcc make

%global debug_package %{nil}

%description
%{summary}

%prep
%autosetup -n %{name}-%{version}-binary

%build
%make_build

%check

%install
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_includedir}/%{name}.h

%changelog
* Wed Apr 23 2025 Theomund <34360334+theomund@users.noreply.github.com> - 9.2.3-1
- Bump version to the 9.2.3 release.
* Sun Mar 30 2025 Theomund <34360334+theomund@users.noreply.github.com> - 9.2.1-1
- Bump version to the 9.2.1 release.
* Sun Mar 09 2025 Theomund <34360334+theomund@users.noreply.github.com> - 9.1.0-1
- Bump version to the 9.1.0 release.
* Tue Feb 18 2025 Theomund <34360334+theomund@users.noreply.github.com> - 9.0.0-1
- Initial package.
