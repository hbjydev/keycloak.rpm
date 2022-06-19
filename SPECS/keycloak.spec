Name:           keycloak
Version:        18.0.1
Release:        1%{?dist}
Summary:        Open Source Identity and Access Management
BuildArch:	noarch

License:        Apache-2.0
URL:            https://keycloak.org
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.service

Patch1:		keycloak-18.0.1-kcsh-etc-keycloak.patch

BuildRequires:	systemd-rpm-macros

Requires:       java-11-openjdk

Requires(preun):	systemd-units
Requires(postun):	systemd-units
Requires(post): 	systemd-units

%description
Keycloak is an Open Source Identity and Access Management solution for modern Applications and Services.

%prep
%setup -q
%patch1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp -r README.md LICENSE.txt version.txt bin providers themes lib $RPM_BUILD_ROOT/%{_datadir}/%{name}/
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}
cp -r conf $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
cd $RPM_BUILD_ROOT/%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
install -p -m 644 $RPM_SOURCE_DIR/%{name}.service $RPM_BUILD_ROOT/%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files
%config %{_sysconfdir}/%{name}/cache-ispn.xml
%config %{_sysconfdir}/%{name}/keycloak.conf
%config %{_sysconfdir}/%{name}/README.md

%{_datadir}/%{name}/README.md
%{_datadir}/%{name}/LICENSE.txt
%{_datadir}/%{name}/version.txt
%{_datadir}/%{name}/bin/client/keycloak-admin-cli-%{version}.jar
%{_datadir}/%{name}/bin/client/keycloak-client-registration-cli-%{version}.jar
%{_datadir}/%{name}/bin/kcadm.bat
%{_datadir}/%{name}/bin/kcadm.sh
%{_datadir}/%{name}/bin/kc.bat
%{_datadir}/%{name}/bin/kc.sh
%{_datadir}/%{name}/bin/kcreg.bat
%{_datadir}/%{name}/bin/kcreg.sh
%{_datadir}/%{name}/providers/README.md
%{_datadir}/%{name}/themes/README.md
%{_datadir}/%{name}/lib
%{_unitdir}/%{name}.service

%changelog
* Sat Jun 18 2022 Hayden Young
- Initial packaging of Keycloak v18.0.1

