Name:    adcli
Version: 0.9.2
Release: 1%{?dist}
Summary: Active Directory enrollment
License: LGPLv2+
URL:     https://gitlab.freedesktop.org/realmd/adcli
Source0: https://gitlab.freedesktop.org/realmd/adcli/uploads/ea560656ac921b3fe0d455976aaae9be/adcli-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: intltool pkgconfig
BuildRequires: libtool
BuildRequires: gettext-devel
BuildRequires: krb5-devel
BuildRequires: openldap-devel
BuildRequires: libxslt
BuildRequires: xmlto
BuildRequires: make

Requires: cyrus-sasl-gssapi
Conflicts: adcli-doc < %{version}-%{release}

# adcli no longer has a library of development files
# the adcli tool itself is to be used by callers
Obsoletes: adcli-devel < 0.5

%description
adcli is a tool for joining an Active Directory domain using
standard LDAP and Kerberos calls.

%define _hardened_build 1

%prep
%autosetup -p1

%build
autoreconf --force --install --verbose
%configure --disable-static --disable-silent-rules \
%if 0%{?rhel}
    --with-vendor-error-message='Please check\n    https://red.ht/support_rhel_ad \nto get help for common issues.' \
%endif
    %{nil}
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=%{buildroot}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%{_sbindir}/adcli
%doc AUTHORS COPYING ChangeLog NEWS README
%doc %{_mandir}/*/*

%package doc
Summary: adcli documentation
BuildArch: noarch
Conflicts: adcli < %{version}-%{release}

%description doc
adcli is a tool for joining an Active Directory domain using
standard LDAP and Kerberos calls. This package contains its
documentation.

%files doc
%doc %{_datadir}/doc/adcli/*

%changelog
* Fri Oct 21 2022 Sumit Bose <sbose@redhat.com> - 0.9.2-1
- Update to upstream release 0.9.2
  Resolves: rhbz#1991619, rhbz#2111348, rhbz#2133838

* Mon Jun 14 2021 Sumit Bose <sbose@redhat.com> - 0.8.2-12
- [RFE] Allow adcli to create AD user with password as well as set or reset
  existing user password [#1952828]
- [RFE] add option to populate "managed by" computer attribute [#1690920]

* Thu Jun 03 2021 Sumit Bose <sbose@redhat.com> - 0.8.2-11
- Add missing patch for [#1769644]

* Thu Jun 03 2021 Sumit Bose <sbose@redhat.com> - 0.8.2-10
- [RFE] Adcli and Realm Error Code Optimization Request [#1889386]
- [RFE] adcli should allow to modify DONT_EXPIRE_PASSWORD attribute [#1769644]

* Fri Dec 11 2020 Sumit Bose <sbose@redhat,com> - 0.8.2-9
- Typo in CREATE A SERVICE ACCOUNT section of man page of adcli [#1906303]

* Wed Nov 11 2020 Sumit Bose <sbose@redhat.com> - 0.8.2-8
- Add --use-ldaps option to adcli update as well [#1883467]
- Cannot join a pre-staged Computer Account on AD in Custom OU using Delegated
  user [#1734764]
- missing documentation for required AD rights for adcli join and net
  join [#1852080]
- [RFE] Add new mode to just create an AD account to be able to connect to
  LDAP [#1854112]

* Thu Aug 13 2020 Sumit Bose <sbose@redhat.com> - 0.8.2-7
- Improve "-C" option description in man page even more [#1791545]

* Mon Jun 15 2020 Sumit Bose <sbose@redhat.com> - 0.8.2-6
- [abrt] [faf] adcli: raise(): /usr/sbin/adcli killed by 6 [#1806260]
- No longer able to delete computer from AD using adcli [#1846882]
- adcli: presetting $computer in $domain domain failed: Cannot set computer
  password: Authentication error [#1846878]
- Typo in adcli update --help option [#1791611]
- Manpage and help does not explain the use of "-C" option [#1791545]

* Wed Jan 29 2020 Sumit Bose <sbose@redhat.com> - 0.8.2-5
- adcli should be able to Force LDAPS over 636 with AD Access Provider w.r.t
  sssd [#1762420]

* Thu Nov 28 2019 Sumit Bose <sbose@redhat.com> - 0.8.2-4
- adcli update --add-samba-data does not work as expected [#1745931]
- Issue is that with arcfour-hmac as first encryption type [#1745932]
- [RFE] enhancement adcli to set description attribute and to show all AD
  attributes [#1737342]

* Fri Jun 14 2019 Sumit Bose <sbose@redhat.com> - 0.8.2-3
- use autosetup macro to simplify patch handling
- fixed rpmlint warnings in the spec file
- join failed if hostname is not FQDN [#1677194]
- adcli join fails in FIPS enabled environment [#1717355]
- forward port of RHEL-7.7 fixes and enhancements

* Tue Oct 09 2018 Sumit Bose <sbose@redhat.com> - 0.8.2-2
- Do not add service principals twice and related fixes
- Resolves: rhbz#1631734

* Thu Jul 05 2018 Sumit Bose <sbose@redhat.com> - 0.8.2-1
- Update to upstream release 0.8.2
- various other fixes and improvements from the latest Fedora update

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 17 2015 Sumit Bose <sbose@redhat.com> - 0.8.0-1
- Update to upstream release 0.8.0

* Mon Oct 19 2015 Stef Walter <stefw@redhat.com> - 0.7.6-1
- Fix issue with keytab use with sshd
- Resolves: rhbz#1267319
- Put documentation in a subpackage

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 30 2014 Stef Walter <stefw@redhat.com> - 0.7.5-2
- Fix incorrect ownership of manual page directory

* Fri Sep 13 2013 Stef Walter <stefw@redhat.com> - 0.7.5-1
- Update to upstream point release 0.7.5
- Workaround for discovery via IPv6 address
- Correctly put IPv6 addresses in temporary krb5.conf

* Mon Sep 09 2013 Stef Walter <stefw@redhat.com> - 0.7.4-1
- Update to upstream point release 0.7.4
- Correctly handle truncating long host names
- Try to contact all available addresses for discovery
- Build fixes

* Wed Aug 07 2013 Stef Walter <stefw@redhat.com> - 0.7.3-1
- Update to upstream point release 0.7.3
- Don't try to set encryption types on Windows 2003

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Stef Walter <stefw@redhat.com> - 0.7.2-1
- Update to upstream point release 0.7.2
- Part of fix for bug [#961244]

* Mon Jul 15 2013 Stef Walter <stefw@redhat.com> - 0.7.1-4
- Build with verbose output logging

* Tue Jun 11 2013 Stef Walter <stefw@redhat.com> - 0.7.1-3
- Run 'make check' when building the package

* Mon May 13 2013 Stef Walter <stefw@redhat.com> - 0.7.1-2
- Bump version to get around botched update

* Mon May 13 2013 Stef Walter <stefw@redhat.com> - 0.7.1-1
- Update to upstream 0.7.1 release
- Fix problems with salt discovery [#961399]

* Mon May 06 2013 Stef Walter <stefw@redhat.com> - 0.7-1
- Work around broken krb5 with empty passwords [#960001]
- Fix memory corruption issue [#959999]
- Update to 0.7, fixing various bugs

* Mon Apr 29 2013 Stef Walter <stefw@redhat.com> - 0.6-1
- Update to 0.6, fixing various bugs

* Wed Apr 10 2013 Stef walter <stefw@redhat.com> - 0.5-2
- Add appropriate Obsoletes line for libadcli removal

* Wed Apr 10 2013 Stef Walter <stefw@redhat.com> - 0.5-1
- Update to upstream 0.5 version
- No more libadcli, and thus no adcli-devel
- Many new adcli commands
- Documentation

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 12 2012 Stef Walter <stefw@redhat.com> - 0.4-1
- Update for 0.4 version, fixing various bugs

* Sat Oct 20 2012 Stef Walter <stefw@redhat.com> - 0.3-1
- Update for 0.3 version

* Tue Sep 4 2012 Stef Walter <stefw@redhat.com> - 0.2-1
- Update for 0.2 version

* Wed Aug 15 2012 Stef Walter <stefw@redhat.com> - 0.1-1
- Initial 0.1 package
