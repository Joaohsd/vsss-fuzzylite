#include <fl/Headers.h>

int main() {
    // Load FLL file
    fl::Engine* engine = fl::FllImporter().fromFile("teste.fll");

    if (engine->isReady() == false) {
        std::cerr << "Error loading FLL file" << std::endl;
        return 1;
    }

    // Create input and output variables
    fl::InputVariable* distancia = engine->getInputVariable("distancia");
    fl::InputVariable* delta_distancia = engine->getInputVariable("delta_distancia");
    fl::OutputVariable* aceleracao = engine->getOutputVariable("aceleracao");

    // Create a fuzzy inference system
    //fl::FuzzySystem fuzzySystem(engine);

    // Set input values
    distancia->setValue(300);
    delta_distancia->setValue(-25);

    // Execute the fuzzy inference
    engine->process();

    // Get output value
    double outputValue = aceleracao->getValue();

    // Print the output value
    std::cout << "Aceleracao: " << outputValue << std::endl;

    return 0;
}
