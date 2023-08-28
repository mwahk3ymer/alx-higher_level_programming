#include <Python.h>

void print_python_list(PyObject *p) {
    if (PyList_Check(p)) {
        Py_ssize_t size = PyList_GET_SIZE(p);
        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        // Print more information as needed
    } else {
        fprintf(stderr, "Invalid PyListObject\n");
    }
}

#include <Python.h>

void print_python_bytes(PyObject *p) {
    if (PyBytes_Check(p)) {
        printf("[.] bytes object info\n");
        printf("  size: %ld\n", PyBytes_GET_SIZE(p));
        printf("  trying string: %s\n", PyBytes_AsString(p));
    } else {
        fprintf(stderr, "Invalid PyBytesObject\n");
    }
}

#include <Python.h>

void print_python_float(PyObject *p) {
    if (PyFloat_Check(p)) {
        printf("[.] float object info\n");
        printf("  value: %f\n", PyFloat_AS_DOUBLE(p));
    } else {
        fprintf(stderr, "Invalid PyFloatObject\n");
    }
}
