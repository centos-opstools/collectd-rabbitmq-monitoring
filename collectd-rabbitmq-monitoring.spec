# Created by pyp2rpm-3.3.2
%global pypi_name collectd-rabbitmq-monitoring
%if 0%{?rhel}==7 || (0%{?fedora} > 1 && 0%{?fedora} < 30)
%global with_python2 1
%endif

%if 0%{?rhel}>7 || 0%{?fedora} > 12
%global with_python3 1
%endif

Name:           %{pypi_name}
Version:        0.0.6
Release:        2%{?dist}
Summary:        Collectd plugin for Rabbitmq

License:        ASL 2.0
URL:            https://github.com/centos-opstools/collectd-rabbitmq-monitoring
Source0:        https://github.com/centos-opstools/collectd-rabbitmq-monitoring/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch


BuildRequires:  git

%description
This plugin provides metrics from a running Rabbitmq cluster via the rabbitmq
management plugin API

%if 0%{?with_python2} > 0
%package -n     python2-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  python-setuptools

Requires:       python2-pyrabbit2
%description -n python2-%{pypi_name}
This plugin provides metrics from a running Rabbitmq cluster via the rabbitmq
management plugin API
%endif

%if 0%{?with_python3} > 0
%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr)
BuildRequires:  python3dist(setuptools)


Requires:       python3dist(pyrabbit2)
%description -n python3-%{pypi_name}
This plugin provides metrics from a running Rabbitmq cluster via the rabbitmq
management plugin API
%endif


%prep
%autosetup -n %{pypi_name}-%{version} -S git
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
export PBR_VERSION=%{version}
%build
%if 0%{?with_python2} > 0
%{__python2} setup.py build
%endif
%if 0%{?with_python3} > 0
PBR_VERSION=1.0.0 %py3_build
%endif

%install
%if 0%{?with_python2} > 0
%{__python2} setup.py install --skip-build --root %{buildroot}
%endif
%if 0%{?with_python3} > 0
%py3_install
%endif

%if 0%{?with_python2} > 0
%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/collectd_rabbitmq_monitoring
%{python2_sitelib}/collectd_rabbitmq_monitoring-*.egg-info
%endif

%if 0%{?with_python3} > 0
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
#%{python3_sitelib}/collectd_rabbitmq_monitoring
#%{python3_sitelib}/collectd_rabbitmq_monitoring-*.egg-info
%endif

%changelog
* Thu Dec 13 2018 Matthias Runge <mrunge@redhat.com> - 0.0.6-2
- add missing BR git

* Fri Dec 07 2018 Matthias Runge <mrunge@redhat.com> - 0.0.6-1
- update to 0.0.6 release

* Fri Oct 26 2018 Matthias Runge <mrunge@redhat.com> - 0.0.5-1
- Initial package.
