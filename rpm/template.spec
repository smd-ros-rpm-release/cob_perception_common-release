Name:           ros-indigo-cob-object-detection-msgs
Version:        0.6.2
Release:        0%{?dist}
Summary:        ROS cob_object_detection_msgs package

Group:          Development/Libraries
License:        LGPL
URL:            http://wiki.ros.org/cob_object_detection_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs

%description
This package contains the cob_object_detection_msgs.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Sep 01 2014 Richard Bormann <rmb@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

* Tue Aug 26 2014 Richard Bormann <rmb@ipa.fhg.de> - 0.5.5-0
- Autogenerated by Bloom

* Thu Aug 28 2014 Richard Bormann <rmb@ipa.fhg.de> - 0.6.1-0
- Autogenerated by Bloom

* Fri Aug 29 2014 Richard Bormann <rmb@ipa.fhg.de> - 0.6.1-2
- Autogenerated by Bloom

* Fri Aug 29 2014 Richard Bormann <rmb@ipa.fhg.de> - 0.6.1-1
- Autogenerated by Bloom

