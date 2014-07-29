%global packname  survival
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.37.7
Release:          1
Summary:          Survival Analysis
Group:            Sciences/Mathematics
License:          LGPLv2+
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.37-7.tar.gz

Requires:         R-stats R-utils R-graphics R-splines 


BuildRequires:    R-devel Rmath-devel R-stats R-utils R-graphics R-splines


%description
survival analysis: descriptive statistics, two-sample tests, parametric
accelerated failure models, Cox model. Delayed entry (truncation) allowed
for all models; interval censoring for parametric models. Case-cohort

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%{rlibdir}/%{packname}