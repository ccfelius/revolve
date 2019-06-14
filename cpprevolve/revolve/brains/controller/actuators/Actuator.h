//
// Created by matteo on 14/06/19.
//

#ifndef REVOLVE_ACTUATOR_H
#define REVOLVE_ACTUATOR_H

namespace revolve {

class Actuator
{
public:
    explicit Actuator(unsigned int n_outputs, double x, double y, double z)
            : Actuator(n_outputs, {x,y,z})
    {}
    explicit Actuator(unsigned int n_outputs, const std::tuple<double, double, double> coordinates)
            : _n_outputs(n_outputs)
            , coordinates(coordinates)
    {}

    inline double coordinate_x() { return std::get<0>(this->coordinates); }
    inline double coordinate_y() { return std::get<1>(this->coordinates); }
    inline double coordinate_z() { return std::get<2>(this->coordinates); }

    virtual void write(const double *output, double step) = 0;

    inline unsigned int n_outputs() const {return this->_n_outputs;}

private:
    const unsigned int _n_outputs;
    const std::tuple<double, double, double> coordinates;
};

}


#endif //REVOLVE_ACTUATOR_H
