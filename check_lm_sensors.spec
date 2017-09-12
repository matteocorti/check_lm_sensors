%define version         3.1.0
%define release         0
%define sourcename      check_lm_sensors
%define packagename     nagios-plugins-check-lm-senors  
%define name    check_lm_sensors
%define nagiospluginsdir %{_libdir}/nagios/plugins

Summary:   A Nagios plugin to monitor sensors values
Name:      %{name}
Version:   %{version}
Release:   %{release}
License:   GPL
Packager:  Matteo Corti <matteo.corti@id.ethz.ch>
Group:     Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source:    https://github.com/matteocorti/check_lm_sensors/files/109583/check_lm_sensors-3.1.0.tar.gz

BuildArch: noarch

Requires:       nagios-plugins
Requires:       hddtemp

# Fedora build requirement (not needed for EPEL{4,5})
BuildRequires: perl(ExtUtils::MakeMaker)

%description
check_lm_sensors is a Nagios plugin to monitor the values of on board sensors and hard
disk temperatures on Linux systems

%prep
%setup -q

%build
%__perl Makefile.PL  INSTALLSCRIPT=%{buildroot}%{_prefix} INSTALLSITEMAN3DIR=%{buildroot}/usr/share/man/man3 INSTALLSITESCRIPT=%{buildroot}%{_prefix}

%install
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0644)
%doc AUTHORS Changes NEWS README INSTALL TODO COPYING VERSION
%attr(0755, root, root) %{_prefix}/check_lm_sensors
%attr(0755, root, root) /usr/share/man/man3/%{name}.3pm.gz

%changelog
* Mon Sep 11 2017 Fredrik Mikker <fredrik@mikker.se> - 3.1.0-1
- adding support for Monitoring::Plugins

* Tue Jun 10 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 3.1.0-0
- repackaging and cleanup

* Thu Oct  4 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 3.0.1-0
- packaged version 3.0.1

* Wed Oct  3 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 3.0.0-2
- added the perl-Nagios-Plugin dependency

* Wed Oct  3 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 3.0.0-1
- included the updated ChangeLog and NEWS files

* Wed Oct  3 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 3.0.0-0
- Upgraded to 3.0.0

* Tue Jul 10 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 2.0-1
- updated to 2.0

* Wed Jun 20 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.1-4
- Requires perl and hddtemp

* Mon Jun 18 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0-0
- Initial release
