Name:       gtest
Summary:    gtest library
Version:    1.2.1.0
Release:    2
License:    TO_BE/FILLED_IN
Vendor:     TO_BE/FILLED_IN
Group:      TO_BE/FILLED_IN
Source0:    %{name}-%{version}.tar.gz
Source1001: 	gtest.manifest
BuildRoot:  %{_tmppath}/%{name}-%{version}-build
BuildRequires: pkgconfig(python)
#BuildRequires: automake autoconf libtool
Provides:   libgtest_main.so.0 libgtest.so.0

%description
gtest library.

%package devel
Summary:    gtest (Development)
Group:      TO_BE/FILLED_IN
Requires:   %{name} = %{version}-%{release}

%description devel
gtest library (DEV)

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
