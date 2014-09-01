Name:           ros-hydro-cob-vision-utils
Version:        0.5.11
Release:        0%{?dist}
Summary:        ROS cob_vision_utils package

Group:          Development/Libraries
License:        LGPL
URL:            http://wiki.ros.org/cob_vision_utils
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-opencv2
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-visualization-msgs
Requires:       tinyxml-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-opencv2
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-visualization-msgs
BuildRequires:  tinyxml-devel

%description
This package contains utilities used within the cob_object_detection toolchain.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Sep 01 2014 Jan Fischer <jsf@ipa.fhg.de> - 0.5.11-0
- Autogenerated by Bloom

* Tue Aug 26 2014 Jan Fischer <jsf@ipa.fhg.de> - 0.5.4-2
- Autogenerated by Bloom

* Thu Aug 28 2014 Jan Fischer <jsf@ipa.fhg.de> - 0.5.6-2
- Autogenerated by Bloom

* Thu Aug 28 2014 Jan Fischer <jsf@ipa.fhg.de> - 0.5.6-1
- Autogenerated by Bloom

* Thu Aug 28 2014 Jan Fischer <jsf@ipa.fhg.de> - 0.5.6-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Jan Fischer <jsf@ipa.fhg.de> - 0.5.4-1
- Autogenerated by Bloom

* Mon Aug 25 2014 Jan Fischer <jsf@ipa.fhg.de> - 0.5.4-0
- Autogenerated by Bloom

* Fri Aug 29 2014 Jan Fischer <jsf@ipa.fhg.de> - 0.5.10-1
- Autogenerated by Bloom

* Fri Aug 29 2014 Jan Fischer <jsf@ipa.fhg.de> - 0.5.10-0
- Autogenerated by Bloom

