#
# Conditional build:
%bcond_without	tests	# unit tests

%define		pnam	Glib
Summary:	Perl Glib bindings
Summary(pl.UTF-8):	Wiązania Glib dla Perla
Name:		perl-Glib
# note: versions 1.x[13579]y are unstable, if you want them, please use DEVEL branch
Version:	1.329_4
%define	fver	%(echo %{version} | tr -d _)
Release:	3
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	https://downloads.sourceforge.net/gtk2-perl/%{pnam}-%{fver}.tar.gz
# Source0-md5:	ee0b309a6d87f7ede45f05787de1901d
URL:		https://gtk2-perl.sourceforge.net/
BuildRequires:	glib2-devel >= 1:2.24.0
BuildRequires:	perl-ExtUtils-Depends >= 0.300
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.06
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Requires:	glib2 >= 1:2.24.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides Perl access to Glib and GLib's GObject libraries.

%description -l pl.UTF-8
Ten moduł daje dostęp z poziomu Perla do bibliotek GLib i GObject.

%package devel
Summary:	Development files for Perl Glib bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Glib dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.24.0

%description devel
Development files for Perl Glib bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Glib dla Perla.

%prep
%setup -q -n %{pnam}-%{fver}

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%{perl_vendorarch}/Glib.pm
%dir %{perl_vendorarch}/Glib
%{perl_vendorarch}/Glib/Object
%dir %{perl_vendorarch}/auto/Glib
%attr(755,root,root) %{perl_vendorarch}/auto/Glib/Glib.so
%{_mandir}/man3/Glib.3pm*
%{_mandir}/man3/Glib::BookmarkFile.3pm*
%{_mandir}/man3/Glib::Boxed.3pm*
%{_mandir}/man3/Glib::Bytes.3pm*
%{_mandir}/man3/Glib::Error.3pm*
%{_mandir}/man3/Glib::Flags.3pm*
%{_mandir}/man3/Glib::KeyFile.3pm*
%{_mandir}/man3/Glib::Log.3pm*
%{_mandir}/man3/Glib::MainLoop.3pm*
%{_mandir}/man3/Glib::Markup.3pm*
%{_mandir}/man3/Glib::Object*.3pm*
%{_mandir}/man3/Glib::OptionContext.3pm*
%{_mandir}/man3/Glib::OptionGroup.3pm*
%{_mandir}/man3/Glib::Param::*.3pm*
%{_mandir}/man3/Glib::ParamSpec.3pm*
%{_mandir}/man3/Glib::Signal.3pm*
%{_mandir}/man3/Glib::Type.3pm*
%{_mandir}/man3/Glib::Utils.3pm*
%{_mandir}/man3/Glib::Variant.3pm*
%{_mandir}/man3/Glib::VariantDict.3pm*
%{_mandir}/man3/Glib::VariantType.3pm*
%{_mandir}/man3/Glib::index.3pm*
%{_mandir}/man3/Glib::version.3pm*
# for Gnome2-related packages
%dir %{perl_vendorarch}/Gnome2
%dir %{perl_vendorarch}/auto/Gnome2

%files devel
%defattr(644,root,root,755)
%{perl_vendorarch}/Glib/CodeGen.pm
%{perl_vendorarch}/Glib/GenPod.pm
%{perl_vendorarch}/Glib/Install
%{perl_vendorarch}/Glib/MakeHelper.pm
%{perl_vendorarch}/Glib/ParseXSDoc.pm
%{_mandir}/man3/Glib::CodeGen.3pm*
%{_mandir}/man3/Glib::GenPod.3pm*
%{_mandir}/man3/Glib::MakeHelper.3pm*
%{_mandir}/man3/Glib::ParseXSDoc.3pm*
%{_mandir}/man3/Glib::devel.3pm*
%{_mandir}/man3/Glib::xsapi.3pm*
