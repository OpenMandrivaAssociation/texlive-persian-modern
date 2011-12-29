# revision 23959
# category Package
# catalog-ctan /fonts/persian-modern
# catalog-date 2011-09-14 17:59:09 +0200
# catalog-license ofl
# catalog-version 0.3
Name:		texlive-persian-modern
Version:	0.3
Release:	1
Summary:	The "Persian Modern" family of fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/persian-modern
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/persian-modern.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/persian-modern.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/persian-modern.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Persian Modern family consists of 12 fonts (based on the
"FarsiTeX Scientific fonts" released into the public domain by
the FarsiTeX project). The single set of fonts is available in
TrueType format (.ttf). Support may be available via the
ParsiLaTeX forum.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/truetype/public/persian-modern/persian-modern-bold.ttf
%{_texmfdistdir}/fonts/truetype/public/persian-modern/persian-modern-bolditalic.ttf
%{_texmfdistdir}/fonts/truetype/public/persian-modern/persian-modern-boldoblique.ttf
%{_texmfdistdir}/fonts/truetype/public/persian-modern/persian-modern-italic.ttf
%{_texmfdistdir}/fonts/truetype/public/persian-modern/persian-modern-italicoutline.ttf
%{_texmfdistdir}/fonts/truetype/public/persian-modern/persian-modern-italicshadow.ttf
%{_texmfdistdir}/fonts/truetype/public/persian-modern/persian-modern-oblique.ttf
%{_texmfdistdir}/fonts/truetype/public/persian-modern/persian-modern-obliqueoutline.ttf
%{_texmfdistdir}/fonts/truetype/public/persian-modern/persian-modern-obliqueshadow.ttf
%{_texmfdistdir}/fonts/truetype/public/persian-modern/persian-modern-outline.ttf
%{_texmfdistdir}/fonts/truetype/public/persian-modern/persian-modern-regular.ttf
%{_texmfdistdir}/fonts/truetype/public/persian-modern/persian-modern-shadow.ttf
%doc %{_texmfdistdir}/doc/fonts/persian-modern/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/persian-modern/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/persian-modern/README
#- source
%doc %{_texmfdistdir}/source/fonts/persian-modern/persian-modern-bold.sfd
%doc %{_texmfdistdir}/source/fonts/persian-modern/persian-modern-bolditalic.sfd
%doc %{_texmfdistdir}/source/fonts/persian-modern/persian-modern-boldoblique.sfd
%doc %{_texmfdistdir}/source/fonts/persian-modern/persian-modern-italic.sfd
%doc %{_texmfdistdir}/source/fonts/persian-modern/persian-modern-italicoutline.sfd
%doc %{_texmfdistdir}/source/fonts/persian-modern/persian-modern-italicshadow.sfd
%doc %{_texmfdistdir}/source/fonts/persian-modern/persian-modern-oblique.sfd
%doc %{_texmfdistdir}/source/fonts/persian-modern/persian-modern-obliqueoutline.sfd
%doc %{_texmfdistdir}/source/fonts/persian-modern/persian-modern-obliqueshadow.sfd
%doc %{_texmfdistdir}/source/fonts/persian-modern/persian-modern-outline.sfd
%doc %{_texmfdistdir}/source/fonts/persian-modern/persian-modern-regular.sfd
%doc %{_texmfdistdir}/source/fonts/persian-modern/persian-modern-shadow.sfd

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc source %{buildroot}%{_texmfdistdir}
