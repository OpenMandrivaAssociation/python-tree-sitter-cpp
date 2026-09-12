Name:		python-tree-sitter-cpp
Version:	0.23.4
Release:	1
Summary:	Tree-sitter cpp grammar (Python bindings)
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/tree-sitter-cpp
Source0:	https://files.pythonhosted.org/packages/20/2c/4dd63d705a8933543cad9b92ff31be849b164fec91a6eb63475ebc9ce668/tree_sitter_cpp-0.23.4.tar.gz
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	clang
Requires:	python%{pyver}dist(tree-sitter)

%description
Tree-sitter grammar for cpp, compiled from source. Used by
Aider's grep-ast repo-map.

%prep
%autosetup -n tree_sitter_cpp-0.23.4

%build

%install
export CC=clang
python -m pip install \
	--no-deps --no-build-isolation --no-compile \
	--root %{buildroot} --prefix %{_prefix} \
	.

%files
%doc README.md
%license LICENSE
%{python_sitearch}/tree_sitter_cpp*
