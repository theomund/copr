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

Name:          gleam
Version:       1.10.0
Release:       2%{?dist}
Summary:       Friendly language for building type-safe systems that scale
URL:           https://%{name}.run
Source:        https://github.com/%{name}-lang/%{name}/archive/refs/tags/v%{version}.tar.gz
License:       Apache-2.0
BuildRequires: cargo
Requires:      erlang

%global debug_package %{nil}

%description
%{summary}

%prep
%autosetup -n %{name}-%{version}

%build
%make_build build

%check

%install
install -Dm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc README.md

%changelog
* Fri Apr 25 2025 Theomund <34360334+theomund@users.noreply.github.com> - 1.10.0-2
- Build directly from the source code.
* Thu Apr 24 2025 Theomund <34360334+theomund@users.noreply.github.com> - 1.10.0-1
- Initial package.
