%define _name Archive
Summary:	ROX-archive is a program for creating and extracting archives
Summary(pl):	ROX-archive s³u¿y do tworzenia i dekompresji archiwów
Name:		rox-%{_name}
Version:	1.9.4
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/archive-%{version}.tgz
# Source0-md5:	c8468811535076da8e7e1b5f9f0c89ed
URL:		http://rox.sourceforge.net/archive.php3
BuildRequires:	rpm-pythonprov
Requires:	python-pygtk-gtk
Requires:	rox-Lib
%pyrequires_eq  python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appsdir	%{_libdir}/ROX-apps

%description
ROX-archive is a very easy to use program for creating and extracting
archives. You can use this program to compress a directory or file
into a single, smaller file (which can be stored, emailed, etc).

%description -l pl
ROX-archive jest bardzo prostym w u¿yciu programem s³u¿±cym do
tworzenia i dekompresji archiwów. Ten program mo¿esz u¿ywaæ aby
zpakowaæ katalog lub plik do jednego, mniejszego (który mo¿e byæ
przechowywany, wys³any poczt±, itp.)

%prep
%setup -q -n archive-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help

rm -f ../install
cd Archive
install App* *.py $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help

%py_comp $RPM_BUILD_ROOT%{_appsdir}/%{_name}
%py_ocomp $RPM_BUILD_ROOT%{_appsdir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Archive/Help/Changes
%attr(755,root,root) %{_appsdir}/%{_name}/AppRun
%{_appsdir}/%{_name}/AppI*
%{_appsdir}/%{_name}/*.py[co]
%{_appsdir}/%{_name}/Help
%dir %{_appsdir}/%{_name}
