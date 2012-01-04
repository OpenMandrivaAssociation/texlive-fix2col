# revision 17133
# category Package
# catalog-ctan /macros/latex/contrib/fix2col
# catalog-date 2010-02-23 16:16:11 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-fix2col
Version:	20100223
Release:	2
Summary:	Fix miscellaneous two column mode features
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fix2col
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fix2col.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fix2col.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fix2col.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
