%global tl_name fix2col
%global tl_revision 78931

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.04
Release:	%{tl_revision}.1
Summary:	Fix miscellaneous two column mode features
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fix2col
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fix2col.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fix2col.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fix2col.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
OBSOLETE: do not use in new documents. This package will do nothing in
LaTeX formats after 2015/01/01 as the fixes that it implements were
incorporated into the fixltx2e package, which is itself obsolete as
since the 2015/01/01 release these fixes are in the LaTeX format itself.
Fix mark handling so that \firstmark is taken from the first column if
that column has any marks at all; keep two column floats like figure* in
sequence with single column floats like figure.

