Name:           xrdcl-authz-plugin
Version:        1.0
Release:        1%{?dist}
Summary:        Library for xrootd client to pick up WLCG Token

License:        LPGL 3.0
URL:            https://github.com/bbockelm/xrdcl-authz-plugin
Source0:       %{name}-%{version}.tar.gz


BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: xrootd-server-devel

Requires:      xrootd-server
Requires:      xrootd-client

%description


%prep
%setup -q


%build
mkdir build
cd build
%cmake ..
make 

%install
pushd build
rm -rf $RPM_BUILD_ROOT
echo $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
popd

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%{_libdir}/libXrd*
%{_libdir}/xrdcl-authz-plugin
%config %{_sysconfdir}/xrootd/client.plugins.d/authz.conf


%changelog
* Wed May 20 2020 Derek Weitzel <dweitzel@unl.edu> - 1.0-1
- Initial RPM




