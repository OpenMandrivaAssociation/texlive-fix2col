Name:		texlive-fix2col
Version:	38770
Release:	1
Summary:	Fix miscellaneous two column mode features
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fix2col
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fix2col.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fix2col.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fix2col.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Fix mark handling so that \firstmark is taken from the first
column if that column has any marks at all; keep two column
floats like figure* in sequence with single column floats like
figure.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fix2col/fix2col.sty
%doc %{_texmfdistdir}/doc/latex/fix2col/README
%doc %{_texmfdistdir}/doc/latex/fix2col/fix2col.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fix2col/fix2col.dtx
%doc %{_texmfdistdir}/source/latex/fix2col/fix2col.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
