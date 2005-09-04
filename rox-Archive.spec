%define _name Archive
Summary:	ROX-archive is a program for creating and extracting archives
Summary(pl):	ROX-archive s³u¿y do tworzenia i dekompresji archiwów
Name:		rox-%{_name}
Version:	2.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/archive-%{version}.tgz
# Source0-md5:	ee7e91a0a3c4fe2ef811260373bfd0ae
URL:		http://rox.sourceforge.net/phpwiki/index.php/Archive
Requires:	python-pygtk-gtk
Requires:	rox >= 2.3
Requires:	rox-Lib2
%pyrequires_eq  python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_roxdir	%{_libdir}/rox

%description
ROX-archive is a very easy to use program for creating and extracting
archives. You can use this program to compress a directory or file
into a single, smaller file (which can be stored, emailed, etc).

%description -l pl
ROX-archive jest bardzo prostym w u¿yciu programem s³u¿±cym do
tworzenia i dekompresji archiwów. Ten program mo¿esz u¿ywaæ aby
spakowaæ katalog lub plik do jednego, mniejszego (który mo¿e byæ
przechowywany, wys³any poczt±, itp.)

%prep
%setup -q -n archive-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_roxdir}/%{_name}/{Help,Messages}

cd Archive
install .DirIcon AppRun *.xml *.py $RPM_BUILD_ROOT%{_roxdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_roxdir}/%{_name}/Help
install Messages/*.gmo $RPM_BUILD_ROOT%{_roxdir}/%{_name}/Messages

%py_comp $RPM_BUILD_ROOT%{_roxdir}/%{_name}
%py_ocomp $RPM_BUILD_ROOT%{_roxdir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Archive/Help/Changes
%attr(755,root,root) %{_roxdir}/%{_name}/AppRun
%dir %{_roxdir}/%{_name}
%{_roxdir}/%{_name}/.DirIcon
%{_roxdir}/%{_name}/*.xml
%{_roxdir}/%{_name}/*.py[co]
%{_roxdir}/%{_name}/Help
%dir %{_roxdir}/%{_name}/Messages
%lang(de) %{_roxdir}/%{_name}/Messages/de.gmo
%lang(es) %{_roxdir}/%{_name}/Messages/es.gmo
%lang(it) %{_roxdir}/%{_name}/Messages/it.gmo
%lang(zh_CN) %{_roxdir}/%{_name}/Messages/zh_CN.gmo
%lang(zh_TW) %{_roxdir}/%{_name}/Messages/zh_TW.gmo
