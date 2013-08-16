Name:       gtest
Summary:    Google Test Framework
Version:    1.2.1.0
Release:    0
License:    BSD-3-Clause
Group:      Development/Testing
Source0:    %{name}-%{version}.tar.gz
Source1001: gtest.manifest
BuildRequires: pkgconfig(python)
Provides:   libgtest_main.so.0 libgtest.so.0

%description
Libraries for Google's Test Framework for writing C++ Tests

%package devel
Summary:    Devel package for Google Test Framework
Group:      Development/Testing
Requires:   %{name} = %{version}-%{release}

%description devel
This is the development package containing the gtest library

%prep
%setup -q
cp %{SOURCE1001} .

%build
./configure --prefix=/usr
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean  
[ ${RPM_BUILD_ROOT} != "/" ] && rm -rf ${RPM_BUILD_ROOT}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root)
/usr/lib/libgtest_main.so.*
/usr/lib/libgtest.so.*

%files devel
%manifest %{name}.manifest
/usr/include/gtest/*.h
/usr/include/gtest/internal/*.h
/usr/lib/libgtest_main.so
/usr/lib/libgtest.so
/usr/lib/libgtest_main.la
/usr/lib/libgtest_main.a
/usr/lib/libgtest.la
/usr/lib/libgtest.a
/usr/share/aclocal/gtest.m4

%changelog
