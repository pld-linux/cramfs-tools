Summary:	Set of tools which creates and checks cramfs filesytem
Summary(pl.UTF-8):	Zestaw narzędzi do tworzenia i sprawdzania systemu plików cramfs
Name:		cramfs-tools
Version:	2.1
Release:	1
License:	GPL
Group:		Base/Utilities
Source0:	https://github.com/npitre/cramfs-tools/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	d056f7a492a2e167a7d03234d1733aca
URL:		https://github.com/npitre/cramfs-tools
BuildRequires:	zlib-devel
Obsoletes:	cramfs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Set of tools which creates and checks cramfs filesystem.

%description -l pl.UTF-8
Zestaw narzędzi do tworzenia i sprawdzania systemu plików cramfs.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

cp -p mkcramfs cramfsck $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NOTES
%attr(755,root,root) %{_sbindir}/*
