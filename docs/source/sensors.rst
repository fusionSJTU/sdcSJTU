Sensor Configuration
===================

One of the platforms for 4D autonomous radar sensing systems is a data acquisition and fusion platform for unmanned vehicles.
We used a triple electric system chassis vehicle with the sensor layout shown in the figure at the Minhang campus of Shanghai Jiaotong University. 
The data was collected from a research platform and does not represent the setup used in the FUSION product. For sensor locations, please refer to :ref:`sensor-setup`. we publish data for the following sensors:

    .. _sensor-setup:

    .. figure:: figures/figSensorSetup.png
        :align: center
        :alt: Sensor Setup

        Fig. 01: Data Acquisition Platform

Scene planning
--------------

Scene SJTU
********
For the Fusion dataset, we plan to conduct initial data collection at the Minhang campus of Shanghai Jiaotong University, as refer to :ref:`scene-SJTU`. We will divide the school into several key driving areas, where data collection will be conducted.

We will expand to a wider range of scenarios after obtaining permission from the relevant authorities.
    .. _scene-SJTU:

    .. figure:: figures/SJTUscene.png
        :align: center
        :alt: SJTU-scene

        Fig. 02: Shanghai Jiao Tong University


Scene Airport
********
to be supplemented

    .. _scene-airport:

    .. figure:: figures/Airport.png
        :align: center
        :alt: airport-scene

        Fig. 03: Airport

Car setup
---------
The real setup of the sensors is shown in the :ref:`car-setup`, and the overall modular design has a high degree of user customizability. 
The sensors are arranged in layers to reduce overall interference, the strong and weak power systems are isolated from each other to ensure safety, and the single sensor system is independent of other sensors to achieve electromagnetic compatibility.

.. _car-setup:

.. list-table::
    :widths: 50 50
    :header-rows: 0
    :align: center


    * - .. figure:: figures/CarSetupFront.png
          :align: center
          :alt: car-setup-f

          Fig. 04: Car Setup Front
      - .. figure:: figures/CarSetupBack.png
          :align: center
          :alt: car-setup-b

          Fig. 05: Car Setup Back

Sensor Information
------------------

Radar
********
The data collection vehicle is equipped with 8 Continental ARS548 millimeter-wave radars with a 120° field of view and two output channels, Objects and Detection.

    .. _sensor-radar:

    .. figure:: figures/SensorRadar.png
        :align: center
        :alt: sensor-Radar

        Fig. 06: Radar

Lidar
********
We used Innovusion's solid-state LiDAR as the LiDAR data input, with each sensor having a 120° field of view angle.

    .. _sensor-lidar:

    .. figure:: figures/SensorLidar.png
        :align: center
        :alt: sensor-Lidar

        Fig. 07: Lidar

Camera
********

We use SenSing Intelligence's 8-channel 8-megapixel YUV camera to collect RGB data, and hard-synchronize the camera data through the GMSL board, 
where four cameras are wide-angle 120-degree cameras, and four are 60-degree cameras, which are capable of capturing 360-degree images around the bodywork without any dead angle.
    .. _sensor-camera:

    .. figure:: figures/SensorCamera.png
        :align: center
        :alt: sensor-Camera

        Fig. 08: Camera

GNSS
********
to be supplemented

    .. _sensor-gnss:

    .. figure:: figures/SensorGNSS.png
        :align: center
        :alt: sensor-GNSS

        Fig. 09: GNSS

iPC
********
to be supplemented

    .. _sensor-:

    .. figure:: figures/SensoriPC.png
        :align: center
        :alt: sensor-iPC

        Fig. 10: iPC

.. note::

   This project is a joint effort from **Smart Sensor Fusion Laboratory and AI Department at SJTU**.

----------------------------------------------------------------------------------------------------

.. autosummary::
   :toctree: generated

   Sensor Configuration