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
Release:       1%{?dist}
Summary:       Friendly language for building type-safe systems that scale
URL:           https://%{name}.run
Source:        https://github.com/%{name}-lang/%{name}/releases/download/v%{version}/%{name}-v%{version}-x86_64-unknown-linux-musl.tar.gz
License:       Apache-2.0
Requires:      erlang

%global debug_package %{nil}

%description
%{summary}

%prep
%setup -qc

%build

%check

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Thu Apr 24 2025 Theomund <34360334+theomund@users.noreply.github.com> - 1.10.0-1
- Initial package.
