# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate unicode-segmentation

Name:           rust-%{crate}
Version:        1.6.0
Release:        2%{?dist}
Summary:        Grapheme Cluster, Word and Sentence boundaries

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/unicode-segmentation
Source:         %{crates_source}
# Initial patched metadata
# * Update quickcheck to 0.9, https://github.com/unicode-rs/unicode-segmentation/pull/60
Patch0:         unicode-segmentation-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Grapheme Cluster, Word and Sentence boundaries according to Unicode Standard
Annex #29 rules.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE COPYRIGHT
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+no_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no_std-devel %{_description}

This package contains library source intended for building other packages
which use "no_std" feature of "%{crate}" crate.

%files       -n %{name}+no_std-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
rm -vr ./scripts/
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Josh Stone <jistone@redhat.com> - 1.6.0-1
- Update to 1.6.0

* Fri Sep 13 22:04:10 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.0-4
- Update quickcheck to 0.9

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 11:31:15 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.0-2
- Regenerate

* Wed May 15 20:00:27 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-6
- Run tests in infrastructure

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 Josh Stone <jistone@redhat.com> - 1.2.1-4
- Adapt to new packaging

* Mon Sep 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-3
- Bump quickcheck to 0.7

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Josh Stone <jistone@redhat.com> - 1.2.1-1
- Update to 1.2.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-5
- Rebuild for rust-packaging v5

* Mon Jan 01 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-4
- Bump quickcheck to 0.6

* Sat Dec 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-3
- Bump quickcheck to 0.5

* Fri Nov 10 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-2
- Exclude unneeded files

* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-2
- Port to use rust-packaging

* Sat Feb 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Initial package