# revision 34268
# category Package
# catalog-ctan /macros/latex/contrib/l3experimental
# catalog-date 2014-05-07 15:15:43 +0200
# catalog-license lppl1.3
# catalog-version SVN 4742
Name:		texlive-l3experimental
Version:	SVN4742
Release:	3
Summary:	Experimental LaTeX3 concepts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/l3experimental
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3experimental.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3experimental.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3experimental.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The l3experimental packages are a collection of experimental
implementations for aspects of the LaTeX3 kernel, dealing with
higher-level ideas such as the Designer Interface. Some of them
work as stand alone packages, providing new functionality, and
can be used on top of LaTeX2e with no changes to the existing
kernel. The present release includes: xgalley, which controls
boxes receiving text for typesetting. l3regex: kernel support
for regular expression search and replace operations; l3sort:
kernel support for sorting sequences, token lists or comma-
lists, according to user-specified comparison criteria; l3str:
kernel support for string manipulation; l3tl-build: kernel
support for token list building; l3tl_analysis: kernel support
for token list analysis; and xcoffins, which allows the
alignment of boxes using a series of 'handle' positions,
supplementing the simple TeX reference point. All the files of
the bundle are also available in the Subversion (SVN)
repository of the LaTeX3 Project. The bundle on CTAN is based
on a snapshot of the SVN repository on 2013-10-11.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/l3experimental/l3sort/l3sort.sty
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3flag.sty
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3regex-trace.sty
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3regex.sty
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-convert.sty
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-enc-iso88591.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-enc-iso885910.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-enc-iso885911.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-enc-iso885913.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-enc-iso885914.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-enc-iso885915.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-enc-iso885916.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-enc-iso88592.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-enc-iso88593.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-enc-iso88594.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-enc-iso88595.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-enc-iso88596.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-enc-iso88597.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-enc-iso88598.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-enc-iso88599.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-enc-utf16.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-enc-utf32.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-enc-utf8.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-esc-hex.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-esc-name.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-esc-string.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-esc-url.def
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str-format.sty
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3str.sty
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3tl-analysis.sty
%{_texmfdistdir}/tex/latex/l3experimental/l3str/l3tl-build.sty
%{_texmfdistdir}/tex/latex/l3experimental/xcoffins/xcoffins.sty
%{_texmfdistdir}/tex/latex/l3experimental/xgalley/l3galley.sty
%{_texmfdistdir}/tex/latex/l3experimental/xgalley/xgalley.sty
%doc %{_texmfdistdir}/doc/latex/l3experimental/README
%doc %{_texmfdistdir}/doc/latex/l3experimental/l3sort/l3sort.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/l3str/l3flag.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/l3str/l3regex.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/l3str/l3str-convert.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/l3str/l3str-format.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/l3str/l3str.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/l3str/l3tl-analysis.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/l3str/l3tl-build.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/xcoffins/xcoffins.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/xgalley/l3galley.pdf
%doc %{_texmfdistdir}/doc/latex/l3experimental/xgalley/xgalley.pdf
#- source
%doc %{_texmfdistdir}/source/latex/l3experimental/l3sort/l3sort.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/l3sort/l3sort.ins
%doc %{_texmfdistdir}/source/latex/l3experimental/l3str/l3flag.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/l3str/l3regex.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/l3str/l3str-convert.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/l3str/l3str-format.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/l3str/l3str.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/l3str/l3str.ins
%doc %{_texmfdistdir}/source/latex/l3experimental/l3str/l3tl-analysis.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/l3str/l3tl-build.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/xcoffins/xcoffins.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/xcoffins/xcoffins.ins
%doc %{_texmfdistdir}/source/latex/l3experimental/xgalley/l3galley.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/xgalley/xgalley.dtx
%doc %{_texmfdistdir}/source/latex/l3experimental/xgalley/xgalley.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
