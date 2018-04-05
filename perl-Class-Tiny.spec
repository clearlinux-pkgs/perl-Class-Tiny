#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-Tiny
Version  : 1.006
Release  : 1
URL      : http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/Class-Tiny-1.006.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/Class-Tiny-1.006.tar.gz
Summary  : 'Minimalist class construction'
Group    : Development/Tools
License  : Apache-2.0
Requires: perl-Class-Tiny-doc

%description
NAME
Class::Tiny - Minimalist class construction
VERSION
version 1.006
SYNOPSIS
In Person.pm:

%package doc
Summary: doc components for the perl-Class-Tiny package.
Group: Documentation

%description doc
doc components for the perl-Class-Tiny package.


%prep
%setup -q -n Class-Tiny-1.006

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Class/Tiny.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
