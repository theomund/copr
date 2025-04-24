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

Name:          erlang
Version:       27.3.3
Release:       1%{?dist}
Summary:       General-purpose programming language and runtime environment
URL:           https://www.%{name}.org
Source:        https://github.com/%{name}/otp/releases/download/OTP-%{version}/otp_src_%{version}.tar.gz
License:       Apache-2.0
BuildRequires: gcc make ncurses-devel openssl-devel perl sed unixODBC-devel

%global debug_package %{nil}

%description
%{summary}

%prep
%autosetup -n otp_src_%{version}

%build
export ERL_TOP=$(pwd)
%configure --prefix=%{_prefix} --with-ssl-rpath=no
%make_build

%check

%install
%make_install

%files
%{_bindir}/*
%{_libdir}/%{name}/*
%doc README.md
%license LICENSE.txt

%changelog
* Wed Apr 23 2025 Theomund <34360334+theomund@users.noreply.github.com> - 27.3.3-1
- Initial package.
