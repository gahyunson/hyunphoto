import { HandsontableBase } from './custom_change_list.js';


class AttendanceHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['user', 'status'];
        this.initialize();
    }

    headerDict(header) {
        const status_idx = this.tableData.header.indexOf('status');

        const headers = header.map(h => ({
            data: h,
            readOnly: h === 'id' ? true : false,
        }));

        headers[status_idx]['type'] = 'select';
        headers[status_idx]['selectOptions'] = [1, 0];
        headers[status_idx]['defaultValue'] = 1;

        return headers;
    }
}

class BadgeHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['name', 'name_en_us', 'desc', 'desc_en_us', 'icon', 'limited', 'condition'];
        this.initialize();
    }

    headerDict(header) {
        const limited_idx = this.tableData.header.indexOf('limited');
        const headers = header.map(h => ({
            data: h,
            readOnly: h === 'id' || h === 'name' || h === 'desc' ? true : false,
        }));
        headers[limited_idx]['type'] = 'select';
        headers[limited_idx]['selectOptions'] = [1, 0];
        headers[limited_idx]['defaultValue'] = 1;
        return headers;
    }

    getNestedHeaders() {
        return [
            [
                '',
                { label: 'name', colspan: 4, collapsible: true },
                { label: '', colspan: 1, collapsible: true },
                { label: '', colspan: 1, collapsible: true },
                { label: 'desc', colspan: 4, collapsible: true },
                { label: '', colspan: 1, collapsible: true }
            ],
            this.tableData.header
        ];
    }
}


class ChallengeHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['start_date', 'end_date', 'monthlyorweekly', 'estimation']; // 필요
        this.initialize();
    }

    headerDict(header) {
        const monthlyorweekly_idx = this.tableData.header.indexOf('monthlyorweekly');

        const headers = header.map(h => ({
            data: h,
            readOnly: h === 'id' ? true : false
        }));

        headers[monthlyorweekly_idx]['type'] = 'select';
        headers[monthlyorweekly_idx]['selectOptions'] = [1, 0];
        headers[monthlyorweekly_idx]['defaultValue'] = 1;

        return headers;
    }
}


class EstimationHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['name', 'activate', 'result_name', 'result_unit', 'subresult1_name', 'subresult1_unit', 'subresult2_name', 'subresult2_unit', 'subresult3_name', 'subresult3_unit', 'subresult4_name', 'subresult4_unit', 'subresult5_name', 'subresult5_unit'];
        this.initialize();
    }

    headerDict(header) {
        const active_idx = header.indexOf('activate')
        const headers = header.map(h => ({
            data: h,
            readOnly: h == 'id' || h == 'name' || h == 'result_name' || h == 'result_unit' ||
                    h == 'subresult1_name' || h == 'subresult1_unit' || h == 'subresult2_name' ||
                    h == 'subresult2_unit' || h == 'subresult3_name' || h == 'subresult3_unit' ||
                    h == 'subresult4_name' || h == 'subresult4_unit' || h == 'subresult5_name' ||
                    h == 'subresult5_unit' ? true : false,
        }));
        headers[active_idx]['type'] = 'select';
        headers[active_idx]['selectOptions'] = [1, 0];
        headers[active_idx]['defaultValue'] = 1;
        return headers;
    }

    getNestedHeaders() {
        return  [
                    [
                        '',
                        { label: 'name', colspan: 4, collapsible: true },
                        { label: '', colspan: 1, collapsible: true },
                        { label: '', colspan: 1, collapsible: true },
                        { label: '', colspan: 1, collapsible: true },
                        { label: '', colspan: 1, collapsible: true },
                        { label: '', colspan: 1, collapsible: true },
                        { label: 'result_name', colspan: 4, collapsible: true },
                        { label: 'result_unit', colspan: 4, collapsible: true },
                        { label: 'subresult1_name', colspan: 4, collapsible: true },
                        { label: 'subresult1_unit', colspan: 4, collapsible: true },
                        { label: 'subresult2_name', colspan: 4, collapsible: true },
                        { label: 'subresult2_unit', colspan: 4, collapsible: true },
                        { label: 'subresult3_name', colspan: 4, collapsible: true },
                        { label: 'subresult3_unit', colspan: 4, collapsible: true },
                        { label: 'subresult4_name', colspan: 4, collapsible: true },
                        { label: 'subresult4_unit', colspan: 4, collapsible: true },
                        { label: 'subresult5_name', colspan: 4, collapsible: true },
                        { label: 'subresult5_unit', colspan: 4, collapsible: true },
                    ],
                    this.tableData.header,
                ];
    }
}


class GuideVideoHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['title', 'title_en_us', 'desc', 'desc_en_us', 'thumbnail', 'video_src'];
        this.initialize();
    }

    headerDict(header) {
        return header.map(h => ({
            data: h,
            readOnly: h === 'id' || h === 'title' || h === 'desc' ? true : false,
        }));
    }

    getNestedHeaders() {
        return [
            [
                '',
                '',
                { label: 'title', colspan: 4, collapsible: true },
                { label: 'desc', colspan: 4, collapsible: true },
                '',
                '',
                ''
            ],
            this.tableData.header
        ]
    }
}


class InquiryHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['name'];
        // this.requiredCol = ['title', 'content', 'email', 'category', 'user']; // 무엇이 진짜인가?
        this.initialize();
    }
    headerDict(header) {
        return header.map(h => ({
            data: h,
            readOnly: h === 'id' ? true: false,
        }));
    }
}


class InquiryCategoryHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['name', 'name_en_us'];
        this.initialize();
    }

    headerDict(header) {
        return header.map(h => ({
            data: h,
            readOnly: h === 'id' || h === 'name' ? true: false,
        }));
    }

    getNestedHeaders() {
        return [
            [
                '',
                { label: 'name', colspan: 4, collapsible: true },
            ],
            this.tableData.header
        ];
    }
}


class LeagueHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['name'];
        this.initialize();
    }

    headerDict(header) {
        const headers = header.map(h => ({
            data: h,
            readOnly: h === 'id' || h == 'group_ptr' ? true : false
        }));

        return headers;
    }
}


class LeagueUserHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['user', 'email']; //
        this.initialize();
    }

    headerDict(header) {
        const sex_idx = this.tableData.header.indexOf('sex');
        const suser_idx = this.tableData.header.indexOf('suser');
        const isdisabled_idx = this.tableData.header.indexOf('is_disabled');
        const isban_idx = this.tableData.header.indexOf('is_ban');

        const headers = header.map(h => ({
            data: h,
            readOnly: h === 'id' || h === 'user_ptr' ? true : false
        }));

        headers[sex_idx]['type'] = 'select';
        headers[sex_idx]['selectOptions'] = [1, 0];
        headers[sex_idx]['defaultValue'] = 1;

        headers[suser_idx]['type'] = 'select';
        headers[suser_idx]['selectOptions'] = [1, 0];
        headers[suser_idx]['defaultValue'] = 1;

        headers[isdisabled_idx]['type'] = 'select';
        headers[isdisabled_idx]['selectOptions'] = [1, 0];
        headers[isdisabled_idx]['defaultValue'] = 1;

        headers[isban_idx]['type'] = 'select';
        headers[isban_idx]['selectOptions'] = [1, 0];
        headers[isban_idx]['defaultValue'] = 1;
        return headers;
    }
}


class NoticeCategoryHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['name', 'name_en_us']
        this.initialize();
    }

    headerDict(header) {
        return header.map(h => ({
            data: h,
            readOnly: h === 'id' || h === 'name' ? true: false,
        }));
    }

    getNestedHeaders() {
        return [
            [
                '',
                { label: 'name', colspan: 4, collapsible: true },
            ],
            this.tableData.header
        ];
    }
}

class OrganizationHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['group_ptr'];
        this.initialize();
    }

    headerDict(header) {
        const headers = header.map(h => ({
            data: h,
            readOnly: h === 'id' || h == 'group_ptr' ? true : false
        }));

        return headers;
    }
}

class OrganizationNoticeHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['title', 'content', 'category', 'organization']; //
        this.initialize();
    }
}


class ReinforceHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['name', 'name_en_us', 'image', 'supercategory'];
        this.initialize();
    }

    headerDict(header) {
        return header.map(h => ({
            data: h,
            readOnly: h === 'id' || h === 'name' ? true : false,
        }));
    }

    getNestedHeaders() {
        return [
            [
                '',
                { label: 'name', colspan: 4, collapsible: true },
                '',
                '',
                ''
            ],
            this.tableData.header
        ]
    }
}


class ScheduleHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['day', 'cleared', 'plan']; //
        this.initialize();
    }

    headerDict(header) {
        const cleared_idx = this.tableData.header.indexOf('cleared');

        const headers = header.map(h => ({
            data: h,
            readOnly: h === 'id' ? true : false
        }));

        headers[cleared_idx]['type'] = 'select';
        headers[cleared_idx]['selectOptions'] = [1, 0];
        headers[cleared_idx]['defaultValue'] = 1;

        return headers;
    }
}


class SubLeagueHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = [];
        this.initialize();
    }

    headerDict(header) {
        const sex_idx = this.tableData.header.indexOf('sex');

        const headers = header.map(h => ({
            data: h,
            readOnly: h === 'id' ? true : false
        }));

        headers[sex_idx]['type'] = 'select';
        headers[sex_idx]['selectOptions'] = [1, 0];
        headers[sex_idx]['defaultValue'] = 1;

        return headers;
    }
}


class SupercategoryHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['name', 'name_en_us'];
        this.initialize();
    }

    headerDict(header) {
        return header.map(h => ({
            data: h,
            readOnly: h === 'id' || h === 'name' ? true : false,
        }));
    }


    getNestedHeaders() {
        return [
            [
                '',
                { label: 'name', colspan: 4, collapsible: true },
                '',
            ],
            this.tableData.header
        ];
    }
}


class TrainingHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['target_set', 'target_num', 'cleared', 'reinforce', 'schedule', 'rpe', 'rest_time'];
        this.initialize();
    }

    headerDict(header) {
        const cleared_idx = this.tableData.header.indexOf('cleared');

        const headers = header.map(h => ({
            data: h,
            readOnly: h === 'id' ? true : false
        }));

        headers[cleared_idx]['type'] = 'select';
        headers[cleared_idx]['selectOptions'] = [1, 0];
        headers[cleared_idx]['defaultValue'] = 1;

        return headers;
    }
}


class UserHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['name', 'birth', 'height', 'weight', 'sex', 'login_count','language', 'suser', 'is_disabled', 'user', 'organization', 'desc', 'is_ban']; //
        this.initialize();
    }

    headerDict(header) {
        const sex_idx = this.tableData.header.indexOf('sex');
        const suser_idx = this.tableData.header.indexOf('suser');
        const isdisabled_idx = this.tableData.header.indexOf('is_disabled');
        const isban_idx = this.tableData.header.indexOf('is_ban');
        const logincnt_idx = this.tableData.header.indexOf('login_count');

        const headers = header.map(h => ({
            data: h,
            readOnly: h === 'id' || h === 'user_ptr' ? true : false
        }));

        headers[sex_idx]['type'] = 'select';
        headers[sex_idx]['selectOptions'] = [1, 0];
        headers[sex_idx]['defaultValue'] = 1;

        headers[suser_idx]['type'] = 'select';
        headers[suser_idx]['selectOptions'] = [1, 0];
        headers[suser_idx]['defaultValue'] = 1;

        headers[isdisabled_idx]['type'] = 'select';
        headers[isdisabled_idx]['selectOptions'] = [1, 0];
        headers[isdisabled_idx]['defaultValue'] = 1;

        headers[isban_idx]['type'] = 'select';
        headers[isban_idx]['selectOptions'] = [1, 0];
        headers[isban_idx]['defaultValue'] = 1;

        headers[logincnt_idx]['defaultValue'] = 0;
        return headers;
    }
}


class UserBadgeHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['badge', 'user', 'representative'];
        this.initialize();
    }

    headerDict(header) {
        const limited_idx = this.tableData.header.indexOf('representative');
        const headers = header.map(h => ({
            data: h,
            readOnly: h === 'id' ? true : false,
        }));
        headers[limited_idx]['type'] = 'select';
        headers[limited_idx]['selectOptions'] = [1, 0];
        headers[limited_idx]['defaultValue'] = 1;
        return headers;
    }
}

class FCMTokenHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['token'];
        this.initialize();
    }
}

class EstimationResultHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['result', 'subresult1', 'subresult2', 'subresult3', 'subresult4', 'subresult5', 'level', 'estimation', 'group', 'user'];
        this.initialize();
    }
}

class GradingHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['cut1', 'cut2', 'cut3', 'cut4', 'cut5', 'cut6', 'cut7', 'cut8', 'cut9', 'cut10', 'cut11', 'estimation', 'ascending', 'sex'];
        this.initialize();
    }
}

class NoticeHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['title', 'content', 'category'];
        this.initialize();
    }
}

class PlanModelHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['startdate', 'enddate', 'cleared', 'user', 'summary'];
        this.initialize();
    }
}

class ScanResultHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['shoulderMisalignment', 'pelvicMisalignment', 'TurtleNeckLeft', 'TurtleNeckRight',
            'RoundShoulderLeft', 'RoundShoulderRight', 'FrontImage', 'LeftImage', 'RightImage', 'user'];
        this.initialize();
    }
}

class UserAchievementHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['achievement', 'user'];
        this.initialize();
    }
}




const modelName = window.MODEL_NAME;
if (modelName === 'attendance') {
    const hot = new AttendanceHandsontable();
} else if (modelName === 'badge') {
    const hot = new BadgeHandsontable();
} else if (modelName === 'challenge') {
    const hot = new ChallengeHandsontable();
} else if (modelName === 'estimation') {
    const hot = new EstimationHandsontable();
} else if (modelName === 'guidevideo') {
    const hot = new GuideVideoHandsontable();
} else if (modelName === 'inquiry') {
    const hot = new InquiryHandsontable();
} else if (modelName === 'inquirycategory') {
    const hot = new InquiryCategoryHandsontable();
} else if (modelName === 'league') {
    const hot = new LeagueHandsontable();
} else if (modelName === 'leagueuser') {
    const hot = new LeagueUserHandsontable();
} else if (modelName === 'noticecategory') {
    const hot = new NoticeCategoryHandsontable();
} else if (modelName === 'organizationnotice') {
    const hot = new OrganizationNoticeHandsontable();
} else if (modelName === 'organization') {
    const hot = new OrganizationHandsontable();
} else if (modelName === 'reinforce') {
    const hot = new ReinforceHandsontable();
} else if (modelName === 'schedule') {
    const hot = new ScheduleHandsontable();
} else if (modelName === 'subleague') {
    const hot = new SubLeagueHandsontable();
} else if (modelName === 'supercategory') {
    const hot = new SupercategoryHandsontable();
} else if (modelName === 'training') {
    const hot = new TrainingHandsontable();
} else if (modelName === 'user') {
    const hot = new UserHandsontable();
} else if (modelName === 'userbadge') {
    const hot = new UserBadgeHandsontable();
} else if (modelName == 'fcmtoken') {
    const hot = new FCMTokenHandsontable();
} else if (modelName == 'estimationresult') {
    const hot = new EstimationResultHandsontable();
} else if (modelName == 'grading') {
    const hot = new GradingHandsontable();
} else if (modelName == 'notice') {
    const hot = new NoticeHandsontable();
} else if (modelName == 'plan') {
    const hot = new PlanModelHandsontable();
} else if (modelName == 'scanresult') {
    const hot = new ScanResultHandsontable();
} else if (modelName == 'userachievement') {
    const hot = new UserAchievementHandsontable();
} else {
    const hot = new ModelHandsontable();
}