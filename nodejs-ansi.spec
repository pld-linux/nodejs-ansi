Summary:	Node.js native addon build tool
Name:		nodejs-ansi
Version:	0.1.2
Release:	1
License:	MIT
Group:		Libraries
URL:		https://github.com/TooTallNate/ansi.js
Source0:	http://registry.npmjs.org/ansi/-/ansi-%{version}.tgz
# Source0-md5:	a46eec705c14995f8380828ec4f9357a
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ansi.js is a module for Node.js that provides an easy-to-use API for
writing ANSI escape codes to Stream instances. ANSI escape codes are
used to do fancy things in a terminal window, like render text in
colors, delete characters, lines, the entire window, or hide and show
the cursor, and lots more!

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/ansi
cp -pr lib package.json $RPM_BUILD_ROOT%{nodejs_libdir}/ansi

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/ansi
%{_examplesdir}/%{name}-%{version}
