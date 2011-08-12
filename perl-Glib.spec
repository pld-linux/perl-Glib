#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pnam	Glib
%include	/usr/lib/rpm/macros.perl
Summary:	Perl Glib bindings
Summary(pl.UTF-8):	Wiązania Glib dla Perla
Name:		perl-Glib
# note: versions 1.x[13579]y are unstable, if you want them, please use DEVEL branch
Version:	1.224
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://downloads.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	f7fa5397f1f6b921ba3c3c4475ae582b
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	glib2-devel >= 1:2.12.2
BuildRequires:	perl-ExtUtils-Depends >= 0.300
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.06
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	glib2 >= 1:2.12.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides Perl access to Glib and GLib's GObject libraries.

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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Glib/*.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Glib/Param/*.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Glib/.packlist

# these should be moved to -devel, if wanted
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Glib/MakeHelper.pm
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/Glib::MakeHelper.3pm

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
