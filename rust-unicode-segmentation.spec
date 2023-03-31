# check disabled to avoid circular dependency (quickcheck -> unicode-segmentation)
%bcond_with check
%global debug_package %{nil}

%global crate unicode-segmentation

Name:           rust-%{crate}
Version:        1.7.1
Release:        2
Summary:        Grapheme Cluster, Word and Sentence boundaries

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/unicode-segmentation
Source:         %{crates_source}

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
