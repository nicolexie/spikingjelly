'''
event_driven包与其他包完全不同

其他包全部都是基于时间驱动（time-driven），需要逐步仿真，而event_driven包则是事件驱动，使用脉冲响应模型（SRM）

在脉冲响应模型中，电压-时间函数具有确定的解析形式，例如 :math:`v(t) = exp^(-t)`

因此在任意时刻，整个神经网络的状态都可以被直接计算出来

时间通常被当作一个维度（类似于ANN中的通道数），例如取仿真时长为T=500，输入为恒定的1，则
输入可以表示为input_data = torch.ones(size=[T])

同理，n个神经元在整个仿真时长内的电压可以表示为shape=[n, T]的tensor

在时间驱动模型中，t+dt时刻的电压依赖于t时刻的电压（逐步积分），因此是逐步仿真，速度很慢

而在事件驱动中，t时刻的电压直接使用 :math:`v(t)` 函数就可以得到，因此是并行的仿真，速度很快

在脉冲响应模型中，脉冲的产生被定义为 :math:`t=\underset{t}{min}{v(t)>v_{threshold}}` ，即
电压首次过阈值的时刻

这一过程是不可导的，SpikeProp使用了线性化的假设来求导。如果解决了这一过程的求导问题，则
脉冲响应模型非常适合直接使用PyTorch的自动微分机制来训练

'''