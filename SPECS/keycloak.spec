Name:           keycloak
Version:        18.0.1
Release:        1%{?dist}
Summary:        Open Source Identity and Access Management
BuildArch:	noarch

License:        Apache-2.0
URL:            https://keycloak.org
Source0:        %{name}-%{version}.tar.gz
Source1:	%{name}.service

BuildRequires:	java-11-openjdk
Requires:       java-11-openjdk

Requires(preun):	systemd-units
Requires(postun):	systemd-units
Requires(post): 	systemd-units

%description
Keycloak is an Open Source Identity and Access Management solution for modern Applications and Services.

%prep
%setup -q
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system
install -p -m 644 $RPM_SOURCE_DIR/keycloak.service $RPM_BUILD_ROOT/usr/lib/systemd/system/keycloak.service

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/keycloak
cp -r * $RPM_BUILD_ROOT/%{_datadir}/keycloak/
cd $RPM_BUILD_ROOT/%{_datadir}/keycloak

%post
%systemd_post keycloak.service

%preun
%systemd_preun keycloak.service

%postun
%systemd_postun keycloak.service

%files
/usr/share/keycloak/README.md
/usr/share/keycloak/LICENSE.txt
/usr/share/keycloak/version.txt
/usr/share/keycloak/bin/client/keycloak-admin-cli-%{version}.jar
/usr/share/keycloak/bin/client/keycloak-client-registration-cli-%{version}.jar
/usr/share/keycloak/bin/kcadm.bat
/usr/share/keycloak/bin/kcadm.sh
/usr/share/keycloak/bin/kc.bat
/usr/share/keycloak/bin/kc.sh
/usr/share/keycloak/bin/kcreg.bat
/usr/share/keycloak/bin/kcreg.sh
/usr/share/keycloak/conf/cache-ispn.xml
/usr/share/keycloak/conf/keycloak.conf
/usr/share/keycloak/conf/README.md
/usr/share/keycloak/providers/README.md
/usr/share/keycloak/themes/README.md
/usr/share/keycloak/lib
/usr/lib/systemd/system/keycloak.service

%changelog
* Sat Jun 18 2022 Hayden Young
- Initial packaging of Keycloak v18.0.1

