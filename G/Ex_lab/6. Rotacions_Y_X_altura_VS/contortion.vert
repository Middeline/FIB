#version 330 core

layout (location = 0) in vec3 vertex;
layout (location = 2) in vec3 color;

out vec4 frontColor;

uniform mat4 modelViewProjectionMatrix;

uniform float time;
uniform float speed = 0.75;

void main()
{
    float alpha = (vertex.y -0.5) * sin(time);
    if (vertex.y < 0.5) alpha = 0;
    
    mat3 rotacioY = mat3 (
        vec3(1, 0, 0), 
        vec3(0, cos(alpha), -sin(alpha)), 
        vec3(0, sin(alpha), cos(alpha)));
    
    vec3 V = rotacioY * vertex;
    
    frontColor = vec4(color,1.0);
    
    gl_Position = modelViewProjectionMatrix * vec4(V, 1.0);
}
