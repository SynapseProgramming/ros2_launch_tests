#include <rclcpp/rclcpp.hpp>
#include <chrono>
#include <string>
#include <functional>

using namespace std::chrono_literals;

class ParametersClass: public rclcpp::Node
{
  public:
    ParametersClass()
      : Node("parameter_node")
    {
      this->declare_parameter<int>("my_int", 3);
      this->get_parameter("my_int", x);
      respond();
    }
    void respond()
    {
      RCLCPP_INFO(this->get_logger(), "my_int is  %d", x);
    }
  private:
    int x;
};

int main(int argc, char** argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<ParametersClass>());
  rclcpp::shutdown();
  return 0;
}
