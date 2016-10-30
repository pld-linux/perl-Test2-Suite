#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test2
%define		pnam	Suite
%include	/usr/lib/rpm/macros.perl
Summary:	Test2::Suite - Distribution with a rich set of tools built upon the Test2 framework
Name:		perl-Test2-Suite
Version:	0.000060
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/E/EX/EXODIST/Test2-Suite-%{version}.tar.gz
# Source0-md5:	6cb3de0e465300f771c8e0d2b77754d5
URL:		http://search.cpan.org/dist/Test2-Suite/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Importer) >= 0.010
BuildRequires:	perl-Test-Simple >= 1.302032
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rich set of tools, plugins, bundles, etc built upon the Test2 testing
library. If you are interested in writing tests, this is the
distribution for you.

If you want to write something that both exports new functions, and
effects behavior, you should write both a Tools distribution, and a
Plugin distribution, then a Bundle that loads them both. This is
important as it helps avoid the problem where a package exports
much-desired tools, but also produces undesirable side effects.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Test2/Bundle.pm
%{perl_vendorlib}/Test2/Bundle
%{perl_vendorlib}/Test2/Compare.pm
%{perl_vendorlib}/Test2/Compare
%{perl_vendorlib}/Test2/Mock.pm
%{perl_vendorlib}/Test2/Plugin.pm
%{perl_vendorlib}/Test2/Plugin
%{perl_vendorlib}/Test2/Require.pm
%{perl_vendorlib}/Test2/Require
%{perl_vendorlib}/Test2/Suite.pm
%{perl_vendorlib}/Test2/Todo.pm
%{perl_vendorlib}/Test2/Tools.pm
%{perl_vendorlib}/Test2/Tools
%{perl_vendorlib}/Test2/Util
%{_mandir}/man3/Test2*.3pm*
