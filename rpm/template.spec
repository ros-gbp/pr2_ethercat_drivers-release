Name:           ros-hydro-ethercat-hardware
Version:        1.8.15
Release:        0%{?dist}
Summary:        ROS ethercat_hardware package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/ethercat_hardware
Source0:        %{name}-%{version}.tar.gz

Requires:       log4cxx-devel
Requires:       ros-hydro-diagnostic-msgs
Requires:       ros-hydro-diagnostic-updater
Requires:       ros-hydro-eml
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-pluginlib
Requires:       ros-hydro-pr2-hardware-interface
Requires:       ros-hydro-pr2-msgs
Requires:       ros-hydro-realtime-tools
Requires:       ros-hydro-roscpp
BuildRequires:  log4cxx-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-diagnostic-msgs
BuildRequires:  ros-hydro-diagnostic-updater
BuildRequires:  ros-hydro-eml
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-pluginlib
BuildRequires:  ros-hydro-pr2-hardware-interface
BuildRequires:  ros-hydro-pr2-msgs
BuildRequires:  ros-hydro-realtime-tools
BuildRequires:  ros-hydro-roscpp

%description
Package for creating a hardware interface to the robot using the EtherCAT motor
controller/driver

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
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
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Jun 19 2015 Austin Hendrix <ahendrix@willowgarage.com> - 1.8.15-0
- Autogenerated by Bloom

* Tue Sep 30 2014 Austin Hendrix <ahendrix@willowgarage.com> - 1.8.11-0
- Autogenerated by Bloom

