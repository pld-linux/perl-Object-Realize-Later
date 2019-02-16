#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Object
%define		pnam	Realize-Later
%include	/usr/lib/rpm/macros.perl
Summary:	Object::Realize::Later - delayed creation of objects
Summary(pl.UTF-8):	Object::Realize::Later - opóźnione tworzenie obiektów
Name:		perl-Object-Realize-Later
Version:	0.21
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9838d35c80f4f11b6a54f519147ad1a2
URL:		http://search.cpan.org/dist/Object-Realize-Later/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Scalar::Util)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Object::Realize::Later class helps with implementing transparent
on demand realization of object data. This is related to the tricks on
autoloading of data, the lesser known cousin of autoloading of
functionality.

%description -l pl.UTF-8
Klasa Object::Realize::Later pomaga w implementowaniu przezroczystego
realizowania danych obiektowych na żądanie. Jest to związane z trikami
przy automatycznym wczytywaniu danych, czyli mniej znaną pochodną
funkcjonalności automatycznego wczytywania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%dir %{perl_vendorlib}/Object/Realize
%{perl_vendorlib}/Object/Realize/*.pm
%{perl_vendorlib}/Object/Realize/*.pod
%{_mandir}/man3/*
