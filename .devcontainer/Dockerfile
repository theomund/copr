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

FROM quay.io/fedora/fedora:41
RUN dnf copr enable -y mczernek/vale 
RUN dnf install -y \
    bash-completion-2.16 \
    copr-cli-2.0 \
    gcc-14.2.1 \
    git-2.49.0 \
    just-1.40.0 \
    make-4.4.1 \
    rpmdevtools-9.6 \
    rpmlint-2.6.1 \
    vale-3.9.6 \
    yamllint-1.37.0 \
    && dnf clean all
RUN useradd -m developer
USER developer
