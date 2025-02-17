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
Version:       9.0.0
Release:       %autorelease
Summary:       Modern, advanced, portable, multiprotocol bootloader and boot manager
URL:           https://limine-bootloader.org
Source:        file://%{name}-%{version}-binary.tar.gz
License:       BSD-2-Clause
BuildRequires: gcc make

%description
%{summary}

%prep
%autosetup -n %{name}-%{version}-binary

%build
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/limine
%{_datadir}/limine/
%{_includedir}/limine.h

%changelog
%autochangelog
