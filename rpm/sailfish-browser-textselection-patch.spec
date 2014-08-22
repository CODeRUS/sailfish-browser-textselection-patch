Name:       sailfish-browser-textselection-patch

# >> macros
BuildArch: noarch
# << macros

Summary:    Sailfish Browser text selection patch
Version:    0.0.1
Release:    2
Group:      Qt/Qt
License:    TODO
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
Requires:   sailfish-browser >= 1.1.3.2

%description
A sailfish-browser patch enabling text selection on page


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfish-browser-textselection-patch
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfish-browser-textselection-patch
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfish-browser-textselection-patch
# >> files
# << files
