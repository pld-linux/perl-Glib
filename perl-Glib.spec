#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Glib
Summary:	Perl Glib bindings
Summary(pl.UTF-8):	Wiązania Glib dla Perla
Name:		perl-Glib
# note: versions 1.x[13579]y are unstable, if you want them, please use DEVEL branch
Version:	1.222
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	2f1af85d768920625f8d4a3ff9b75cc4
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	glib2-devel >= 1:2.12.2
BuildRequires:	perl-ExtUtils-Depends >= 0.300
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.06
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	glib2 >= 1:2.12.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides perl access to Glib and GLib's GObject libraries.

%description -l pl.UTF-8
Ten moduł daje dostęp z poziomu Perla do bibliotek GLib i GObject.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorarch}/{Gnome2,auto/Gnome2}

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Glib/*.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Glib/Param/*.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Glib/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README*
%{perl_vendorarch}/Glib.pm
%dir %{perl_vendorarch}/Glib
%{perl_vendorarch}/Glib/*.pm
%{perl_vendorarch}/Glib/Install
%{perl_vendorarch}/Glib/Object
%dir %{perl_vendorarch}/auto/Glib
%attr(755,root,root) %{perl_vendorarch}/auto/Glib/Glib.so
%{perl_vendorarch}/auto/Glib/Glib.bs
%{_mandir}/man3/Glib*.3pm*
# for Gnome2-related packages
%dir %{perl_vendorarch}/Gnome2
%dir %{perl_vendorarch}/auto/Gnome2
