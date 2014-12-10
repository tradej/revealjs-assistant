%global shortname revealjs

Name:           dap-%{shortname}
Version:        0.2
Release:        1%{?dist}
Summary:        Reveal.js assistant

BuildArch:      noarch

License:        MIT
URL:            https://github.com/tradej/revealjs-assistant
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       dap-common_args
Requires:       dap-git
Requires:       dap-github

%description
Creates a new Reveal.js presentation with optional Grunt webserver support


%prep
%setup -q -n %{shortname}-%{version}

%build
%repack_assistant

%install
%install_assistant

%check
%check_assistant

%files
%doc %{assistant_path}/doc/%{shortname}
%{assistant_path}/assistants/crt/%{shortname}*
%{assistant_path}/files/crt/%{shortname}*
%{assistant_path}/icons/crt/%{shortname}*
%{assistant_path}/meta/%{shortname}.yaml

%changelog
* Wed Dec 10 2014 Tomas Radej <tradej@redhat.com> - 0.2-1
Initial package
