# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define rpm_device i4113
%define rpm_vendor qualcomm

%define vendor_pretty Sony
%define device_pretty Xperia 10 - Dual SIM

%define have_vibrator_native 1
%define have_led 1

BuildRequires: droid-config-%{rpm_device}
BuildRequires: droid-config-%{rpm_device}-bluez5
BuildRequires: droid-config-%{rpm_device}-flashing
BuildRequires: droid-config-%{rpm_device}-preinit-plugin
BuildRequires: droid-config-%{rpm_device}-pulseaudio-settings
BuildRequires: droid-config-%{rpm_device}-sailfish
BuildRequires: droid-hal-%{rpm_device}
BuildRequires: droid-hal-%{rpm_device}-img-boot
BuildRequires: droid-hal-%{rpm_device}-img-recovery
BuildRequires: droid-hal-%{rpm_device}-kernel
BuildRequires: droid-hal-%{rpm_device}-tools

%include droid-hal-version/droid-hal-version.inc
