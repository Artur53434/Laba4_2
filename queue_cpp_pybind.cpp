#include <pybind11/pybind11.h>
#include <queue>
#include <stdexcept>

namespace py = pybind11;

class CppQueue {
private:
    std::queue<int> q;
    int max_size;
public:
    CppQueue(int ms) : max_size(ms) {}

    bool push(int value) {
        if (q.size() >= max_size) return false;
        q.push(value);
        return true;
    }

    int pop() {
        if (q.empty()) throw std::out_of_range("Queue is empty");
        int val = q.front();
        q.pop();
        return val;
    }

    void clear() {
        while (!q.empty()) q.pop();
    }

    int find(int value) {
        std::queue<int> temp = q;
        for (int i = 0; i < (int)temp.size(); ++i) {
            if (temp.front() == value) return i;
            temp.pop();
        }
        return -1;
    }

    bool is_empty() {
        return q.empty();
    }
};

PYBIND11_MODULE(queue_cpp_pybind, m) {
    m.doc() = "C++ STL Queue module";
    py::class_<CppQueue>(m, "CppQueue")
        .def(py::init<int>(), py::arg("max_size"))
        .def("push", &CppQueue::push)
        .def("pop", &CppQueue::pop)
        .def("clear", &CppQueue::clear)
        .def("find", &CppQueue::find)
        .def("is_empty", &CppQueue::is_empty);
}