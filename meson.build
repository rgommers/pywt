project(
  'PyWavelets',
  'c', 'cython',
  version: '1.7.0.dev0',
  license: 'MIT',
  meson_version: '>= 1.3.0',
  default_options: [
    'buildtype=debugoptimized',
    'b_ndebug=if-release',
    'c_std=c17',
  ],
)

cython = find_program('cython')

py_min_version = '3.12'  # used to set limited C API min version
py = import('python').find_installation(pure: false)
py_dep = py.dependency()

subdir('pywt')
