#ifndef __JOYSTICK_H__
#define __JOYSTICK_H__

#include "Headers.h"
#include "Config.h"

/*enum Joystick_dir
{
	_LEFT,
	_RIGHT,
	_STOP
};*/

class Joystick : public Layer
{
public:
	Joystick();
	~Joystick();

	// ����ҡ�ˣ�aPoint��ҡ������ aRadius��ҡ�˰뾶 aJsSprite��ҡ�˿��Ƶ� aJsBg��ҡ�˱���
	static Joystick* create(Vec2 aPoint, float aRadius, const char* aJsSprite, const char* aJsBg);

	// ��ȡҡ�˷���
	// Joystick_dir getDirection();
	Vec2 getDirection();

	// ��ȡҡ������
	float getVelocity();

private:
	void update(float dt); 
	// ��ʼ����aPoint��ҡ������ aRadius��ҡ�˰뾶 aJsSprite��ҡ�˿��Ƶ� aJsBg��ҡ�˱���
	virtual bool init(Vec2 aPoint ,float aRadius, const char* aJsSprite, const char* aJsBg);
	virtual bool onTouchBegan(Touch *pTouch, Event *pEvent);
	virtual void onTouchMoved(Touch *pTouch, Event *pEvent);
	virtual void onTouchEnded(Touch *pTouch, Event *pEvent);

private:
	Vec2 m_centerPoint;    // ҡ������
	Vec2 m_currentPoint;   // ҡ�˵�ǰλ��
	float m_radius;        // ҡ�˰뾶
	Sprite* m_jsSprite;    //ҡ�˿��Ƶ�
};

#endif
