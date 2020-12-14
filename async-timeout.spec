#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : async-timeout
Version  : 3.0.1
Release  : 15
URL      : https://files.pythonhosted.org/packages/a1/78/aae1545aba6e87e23ecab8d212b58bb70e72164b67eb090b81bb17ad38e3/async-timeout-3.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/a1/78/aae1545aba6e87e23ecab8d212b58bb70e72164b67eb090b81bb17ad38e3/async-timeout-3.0.1.tar.gz
Summary  : Timeout context manager for asyncio programs
Group    : Development/Tools
License  : Apache-2.0
Requires: async-timeout-license = %{version}-%{release}
Requires: async-timeout-python = %{version}-%{release}
Requires: async-timeout-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=============

%package license
Summary: license components for the async-timeout package.
Group: Default

%description license
license components for the async-timeout package.


%package python
Summary: python components for the async-timeout package.
Group: Default
Requires: async-timeout-python3 = %{version}-%{release}

%description python
python components for the async-timeout package.


%package python3
Summary: python3 components for the async-timeout package.
Group: Default
Requires: python3-core
Provides: pypi(async_timeout)

%description python3
python3 components for the async-timeout package.


%prep
%setup -q -n async-timeout-3.0.1
cd %{_builddir}/async-timeout-3.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603387580
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/async-timeout
cp %{_builddir}/async-timeout-3.0.1/LICENSE %{buildroot}/usr/share/package-licenses/async-timeout/92170cdc034b2ff819323ff670d3b7266c8bffcd
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/async-timeout/92170cdc034b2ff819323ff670d3b7266c8bffcd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
